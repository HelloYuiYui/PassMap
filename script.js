var cc = '';//countryCodes();
countryCodes();

function paint(c, color){
	var f = document.getElementsByClassName(c);
	for (i=0;i<f.length;i++){
    	f[i].style.fill = color;
	}
}

function getB(c){
    var x = new XMLHttpRequest();
    x.onreadystatechange=function(){
        if (x.readyState==4 && x.status==200){
            var passdata = JSON.parse(x.responseText);
            paintMap(c, passdata);
        }
    }
    x.open('GET', '/country/' + c, true);
    x.setRequestHeader('Content-Type', 'application/json');
    x.send();
}
    
function countryCodes(){
    var ret = '';
    var x = new XMLHttpRequest();
    x.onreadystatechange=function(){
        if (x.readyState==4){ // && x.status==304){
            cc = JSON.parse(x.responseText);
        }
    }
    x.open('GET', '/codes', true);
    x.setRequestHeader('Content-Type', 'application/json');
    x.send();
    
}

function paintMap(c, ree){
    //paint(cc[ree['self']].toLowerCase(), 'orange');
    var vf = ree['visafree'];
    
    vf.forEach(function(i){
        if (cc[i] == undefined){
            return 0;
            //console.log('an error occured');
        } else {
            //console.log(cc[i].toLowerCase());
            paint(cc[i].toLowerCase(), 'green');
        }
    })
    
    veta = ree['visaeta']
    veta.forEach(function(i){
        if (cc[i] == undefined){
            return 0;
            //console.log('an error occured');
        } else {
            //console.log(cc[i].toLowerCase());
            paint(cc[i].toLowerCase(), 'beffb3');
        }
    })
        
    von = ree['visaonarrival']
    von.forEach(function(i){
        if (cc[i] == undefined){
            return 0;
            //console.log('an error occured');
        } else {
            //console.log(cc[i].toLowerCase());
            paint(cc[i].toLowerCase(), '8ed498');    // 8ed498
        }
    })
    
    // comment here to get a combined result.
    vr = ree['visarequired']
    vr.forEach(function(i){
        if (cc[i] == undefined){
            return 0;
            //console.log('an error occured');
        } else {
            //console.log(cc[i].toLowerCase());
            paint(cc[i].toLowerCase(), 'c0c0c0');    // 8ed498
        }
    })
    
    if (document.getElementById(c).className['animVal'].indexOf(' eu') > 0){ paint('eu', '003399'); }
    
    paint(cc[ree['self']].toLowerCase(), 'orange');
    
    
}

document.addEventListener('click', function(e) {
    e = e || window.event;
    var target = e.target || e.srcElement,
        text = target.textContent || target.innerText;
    if (target.parentNode.tagName == 'svg'){
        getB(target.id)
    } else {
        getB(target.parentNode.id);
    }
    
}, false);