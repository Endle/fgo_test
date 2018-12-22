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

function loadNext(Qs, cur, q) {
}

function loadQuestion(Qs, cur, q) {
    let multiHint = '';
    if (q.ID.match('multi')) {
        multiHint = 'Multiple choices not supported yet!';
    }
    let qBaseStr = `<div id="description">
                        <p>${q.Desc}</p>
                        <div id="hint">${multiHint}</div>
                    </div>`;
    let qEl = $(qBaseStr);
    q.Choices.forEach( function(x){
        let hs = `<input type="radio"
                        class="choice"
                        name="stub" value="${x.description}">
            ${x.description}<br>`;
        /*console.log(x);*/
        qEl.append( $(hs) );
    });
    let submit = $('<input type="submit" value="Next">');
    submit.click( function(e){
        let checkedChoices = $('.choice:checked');
        //apply change of scores
        checkedChoices.each(function(i){
            let _this = this.value;
            let c = q.Choices.find(function(x){
                /*console.log('loop choices');*/
                /*console.log(x.description);console.log(_this);*/
                return x.description===_this;});
            console.log('find chosen item');
            console.log(c);
            for (var i=0; i<cur.D; ++i) {
                cur.score[i] += c.affection[i];
            }
        });
        console.log(cur.score);
        loadNext();
    });
    qEl.append(submit);

    //useless
    var q2 = selectQuestion(Qs, q.ID);
    $('#question').html(JSON.stringify(q2));
    $('#question').append(qEl);
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
