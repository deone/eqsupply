function showQuoteForm(id) {
    $("#cell" + id).find("#quote_btn").hide();
    $("#cell" + id).find("#quote_form").show();
}

function quote(pvId)  {
    alert($("#qty" + pvId).val());
}
