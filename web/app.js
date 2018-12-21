// Qs => questions
$(document).ready(function(){
    $.getJSON("result.json", function(Qs) {
        /*console.log(Qs);*/
        init_vote(Qs);
    });
});

function selectQuestion(Qs, qid){
    return Qs.find(function(e){
        return e.ID === qid;
    });
}

function loadQuestion(Qs, cur, q) {

    //useless
    var q2 = selectQuestion(Qs, q.ID);
    $('#question').html(JSON.stringify(q2));
    return 1;
}

function init_vote(Qs){
    // 这里不太准确。应该是选取数组的第一个元素
    var first = Qs.find(function(e){
        /*$('#question').html( e.Base.toString() );*/
        return e.Base.toString() === '1';
    });
    var cur = {}; //current status
    cur.D = first.Dimension;
    cur['score'] = [];
    for (var i=0; i<cur.D; ++i)
        cur['score'].push(0);
    cur.ID = first.ID;

    /*$('#question').html(JSON.stringify(first));*/
    console.log(JSON.stringify(first));
    console.log(cur);
    loadQuestion(Qs, cur, first);
    return 1;
}
