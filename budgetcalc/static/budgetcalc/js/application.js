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
    $(".budget-builder .input label, .budget-builder .optiongroup")
    .popover()
    $(".budget-builder .clear")
    .popover()
    .on("click", function () {
        var optionGroup = $(this).attr("name");
        $("input[name='" + optionGroup + "']").prop("checked", false);
        updateBudget();
    });

    $(".budget-change").on("change", function() {
        updateBudget();
    });  

    // update budget tally
    var updateBudget = function () {
        budget = {
            "options" : [],
            "gap": 161000000,
            "filled": 0
        };
        $(".budget-change").each(function (){
            if ($(this).prop("checked")) {
                budget["options"].push(parseInt($(this).attr("id").split("_")[1]));
                budget["filled"] += parseInt($(this).val());
                budget["gap"] -= parseInt($(this).val());
            }
        });
        $(".tally .budget-filled").html("$ " + addCommas(budget["filled"]));
        $(".tally .budget-gap").html("$ " + addCommas(budget["gap"]));
        if (budget["gap"] < 0) $(".tally .budget-gap").css("color", "#468847");
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
                $(".page-header .lead").html(data["budget__count"] + " users worked on the MBTA budget gap and filled it by an average of <span class='budget-filled'>$ " + addCommas(parseInt(data["budget__avg"])) + "</span>.<br>See the total number of selections per option below.");
                $.each(data["options"], function(option, nr) {
                    if ($("#option_nr_" + option).length === 0) {
                        $("#option_" + option).parent().prepend("<span id='option_nr_" + option + "' class='label label-info'>&times; " + nr + "</span>");
                    } else {
                        $("#option_nr_" + option).html("&times; " + nr);
                    }
                });
                $(".alert").hide("slow");
                try {
                    $(".twitter-share-button").remove();
                    $(".twitterwidget").prepend("<a href='https://twitter.com/share' class='twitter-share-button' data-text='I worked on the MBTA Budget and filled it by $ " + addCommas(budget['filled']) + "!' data-size='large' data-via='MAPCMetroBoston'>Tweet</a>");
                    // re-evaluate twitter widget
                    twttr.widgets.load();
                } catch (e) {
                    // twitter widget not available
                    $(".twitterwidget").remove();
                }
                $(".email-link .btn").attr("href","mailto:?subject=MBTA Budget Calculator&body=I worked on the MBTA Budget and filled it by $ " + addCommas(budget['filled']) + " - Try yourself at http://fixthet.mapc.org");
                $("html, body").animate({scrollTop:0}, "slow");
            }, 
            "json"
        );
    });

});