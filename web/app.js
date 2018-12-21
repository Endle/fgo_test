// Qs => questions
$(document).ready(function(){
    $.getJSON("result.json", function(Qs) {
        console.log(Qs);
        init_vote(Qs);
    });
});

function init_vote(Qs){
    var first = Qs.find(function(e){
        /*$('#question').html( e.Base.toString() );*/
        return e.Base.toString() === '1';
    });
    $('#question').html(JSON.stringify(first));
    return 1;
}
