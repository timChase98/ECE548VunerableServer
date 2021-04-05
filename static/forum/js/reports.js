var ofs = 0;

window.setInterval(function(){
var elr = document.getElementsByClassName('redFlash');
var elb = document.getElementsByClassName('blueFlash');
for(var i = 0; i < elr.length; i++){
	elr[i].style.background = 'rgba(255,0,0,'+Math.abs(Math.sin(ofs))+')';
}
for(var i = 0; i < elb.length; i++){
	elb[i].style.background = 'rgba(0,0,255,'+Math.abs(Math.sin(ofs))+')';
}
ofs += 0.01;
}, 10);
