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
            console.log(passdata);
            reset(c, passdata);
            paintMap(c, passdata);
        }
    }
    x.open('GET', '/country/' + c, true);
    x.setRequestHeader('Content-Type', 'application/json');
    x.send();
}

function reset(c, passdata){
    for (const [key, value] of Object.entries(passdata)) {
        value.forEach(function(i){
            paint(i.toLowerCase(), '#c0c0c0');
        })
    }
}

function paintMap(c, ree){
    ban = ree['no admission'];
    ban.forEach(function(i){
        if (i == undefined || i == NaN){
            console.log('an error occured = ' + i);
        } else {
            paint(i.toLowerCase(), 'black');
        }
    })

    visa = ree['visarequired'];
    visa.forEach(function(i){
        if (i == undefined || i == NaN){
            console.log('an error occured = ' + i);
        } else {
            paint(i.toLowerCase(), '#c0c0c0');
        }
    })
    
    veta = ree['visaeta'];
    veta.forEach(function(i){
        if (i == undefined || i == NaN){
            console.log('an error occured = ' + i);
        } else {
            paint(i.toLowerCase(), '#beffb3');
        }
    })
    
    voa = ree['visaonarrival'];
    voa.forEach(function(i){
        if (i == undefined || i == NaN){
            console.log('an error occured = ' + i);
        } else {
            paint(i.toLowerCase(), '#8ed498');
        }
    })

    vf = ree['visafree'];
    vf.forEach(function(i){
        if (i == undefined || i == NaN){
            console.log('an error occured = ' + i);
        } else {
            paint(i.toLowerCase(), 'green');
        }
    })

    fom = ree['FoM'];
    fom.forEach(function(i){
        if (i == undefined || i == NaN){
            console.log('an error occured = ' + i);
        } else {
            paint(i.toLowerCase(), '#003399');
        }
    })
    
    // self = ree['self'];
    // self.forEach(function(i){
    //     if (i == undefined || i == NaN){
    //         console.log('an error occured = ' + i);
    //     } else {
    //         paint(i.toLowerCase(), 'orange');
    //     }
    // })
    
    paint(ree["self"][0].toLowerCase(), 'orange');
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