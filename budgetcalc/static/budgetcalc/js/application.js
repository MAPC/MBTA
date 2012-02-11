jQuery(document).ready(function($) {

    $('.budget-builder .clear')
    .popover({
        title: "Clear this options",
        content: "Removes your selections from this section"
    })
    .on("click", function () {
        var optionGroup = $(this).attr("name");
        $("input[name='" + optionGroup + "']").prop("checked", false);
        updateBudget();
    });

    $(".budget-change").on("change", function() {
        updateBudget();
    });  

    // update budget figures
    var updateBudget = function () {
        var budgetMissing = 161000000;
        var budgetFilled = 0;
        $(".budget-change").each(function (){
            if ($(this).prop("checked")) {
                budgetFilled += parseInt($(this).val());
                budgetMissing -= parseInt($(this).val());
            }
        });
        $(".budget-figure .filled").html("$" + addCommas(budgetFilled));
        $(".budget-figure .missing").html("$" + addCommas(budgetMissing));
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

});