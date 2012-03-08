jQuery(document).ready(function($) {

    var budget = {};

    // utils
    // simple validations
    $(".alert").hide();
    $(".alert .close").on('click', function (e) {
        e.preventDefault(); 
        $(this).parent().hide("slow");
    });
    var isEmail = function (email) {
        var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        return regex.test(email);
    }
    // taken from http://www.mredkj.com/javascript/numberFormat.html#addcommas
    var addCommas = function (nStr) {
        nStr += '';
        x = nStr.split('.');
        x1 = x[0];
        x2 = x.length > 1 ? '.' + x[1] : '';
        var rgx = /(\d+)(\d{3})/;
        while (rgx.test(x1)) {
            x1 = x1.replace(rgx, '$1' + ',' + '$2');
        }
        return x1 + x2;
    }

    // form utils
    // popovers
    $(".budget-builder .details")
    .popover();
    $(".budget-builder .clear")
    .on("click", function () {
        var optionGroup = $(this).attr("name");
        $("input[name='" + optionGroup + "']").prop("checked", false);
        // deselect and hide child options
        $("input[data-optiongroup='" + optionGroup + "']").prop("checked", false).parentsUntil("tbody").hide();
        updateBudget();
    });
    $(".budget-change").on("change", function() {
        // parent/child options
        if ($(this).attr("type") === "radio") {
            // child or parent?
            var optionParent = $(this).attr("data-parent");
            if (optionParent) {
                var optionGroup = $(this).attr("data-optiongroup"); 
                var optionId = $(this).attr("data-parent"); 
            } else {
                var optionGroup = $(this).attr("name");
                var optionId = $(this).attr("id");
            }
            // deselect all checked options in that optiongroup
            $("input[name='" + optionGroup + "']").prop("checked", false);
            $("input[data-optiongroup='" + optionGroup + "']").prop("checked", false);
            // hide all child options in that optiongroup
            $("input[data-optiongroup='" + optionGroup + "']").parentsUntil("tbody").hide();
            // select option and show all related child options
            $("input[name='" + optionId + "-child']").parentsUntil("tbody").show();
            $("input[name='" + optionId + "-child']").first().prop("checked", true);   
            // select clicked option
            $(this).prop("checked", true);
            // select parent option
            if (optionParent) $("#" + optionParent).prop("checked", true); 
        }  
        // recalculate
        updateBudget();
    }); 
    // hide all child options 
    $.each($("input[name$='-child']"), function (index, value) {
        $(value).parentsUntil("tbody").hide();
    });

    // update budget tally
    var updateBudget = function () {
        budget = {
            "options" : [],
            "gap": -161000000,
            "filled": 0
        };
        $(".budget-change").each(function (){
            if ($(this).prop("checked")) {
                budget["options"].push(parseInt($(this).attr("id").split("_")[1]));
                budget["filled"] += parseInt($(this).val());
                budget["gap"] += parseInt($(this).val());
            }
        });
        if (budget["gap"] < 0) {
            $(".tally .budget-gap").css("color", "#B94A48");
            $(".budget-gap-verbose").html("Deficit");
        } else {
            $(".tally .budget-gap").css("color", "#333");
            $(".budget-gap-verbose").html("Surplus");
        }
        $(".tally .budget-filled").html("$ " + addCommas(budget["filled"]));
        $(".tally .budget-gap").html("$ " + addCommas(Math.abs(budget["gap"])));
        if ($("#error-nobudget").is(':visible')) $("#error-nobudget").hide("slow");
    }

    // submit budget
    $("#budget-form").on("submit", function (e) {
        e.preventDefault(); 

        budget["email"] = $("form #email").val();
        
        // some simple validations
        if (!budget["filled"]) {
            $("#error-nobudget").show("slow");
            return false;
        }
        if (!isEmail(budget["email"])) {
            $("#error-noemail").show("slow");
            return false;   
        }

        budget["csrfmiddlewaretoken"] = $("input[name='csrfmiddlewaretoken']").val();
        budget["options"] = (typeof budget["options"] === 'object') ? JSON.stringify(budget["options"]) : budget["options"];

        $.post($(this).attr("action"), 
            budget,
            function (data) {
                // some result stats
                $(".page-header .lead").html("You are one of " + data["budget__count"] + " users to come up with your own plan to fix the T's budget. Budget proposals so far have had an average combined revenue and savings of <span class='budget-filled'>$ " + addCommas(parseInt(data["budget__avg"])) + "</span>.<br>See how many people chose each option below.");
                $.each(data["options"], function(option, nr) {
                    if ($("#option_nr_" + option).length === 0) {
                        $("#option_" + option).parent().prepend("<span id='option_nr_" + option + "' class='label label-info'>&times; " + nr + "</span>");
                    } else {
                        $("#option_nr_" + option).html("&times; " + nr);
                    }
                });
                // move buttons to the top
                $(".alert").hide("slow");
                $("header.page-header").after($("section.social-media"));
                $("header.page-header").after($("section.dia"));

                // workaround for non-available twitter resources
                try {
                    $(".twitter-share-button").remove();
                    $(".twitterwidget").prepend("<a href='https://twitter.com/share' class='twitter-share-button' data-url='http://fixthet.mapc.org/' data-text='I came up with my own plan to fix the MBTA Budget and filled the gap by $ " + addCommas(budget['filled']) + "!' data-via='MAPCMetroBoston'>Tweet</a>");
                    // re-evaluate twitter widget
                    twttr.widgets.load();
                } catch (e) {
                    // twitter widget not available
                    $(".twitterwidget").remove();
                }

                // update email link
                $(".email-link .btn").attr("href","mailto:?subject=MBTA Budget Calculator&body=I came up with my own plan to fix the MBTA Budget and filled the gap by $ " + addCommas(budget['filled']) + ". Try yourself at http://fixthet.mapc.org");

                // update submit button
                $("#budget-btn").html("Re-Submit Your Proposal");

                // show all child options 
                $.each($("input[name$='-child']"), function (index, value) {
                    $(value).parentsUntil("tbody").show();
                });

                $("html, body").animate({scrollTop:0}, "slow");
            }, 
            "json"
        );
    });

});