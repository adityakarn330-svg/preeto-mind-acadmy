(function(){
  var body=document.body;
  var toggle=document.querySelector('.menu-toggle');
  if(toggle){toggle.addEventListener('click',function(){
    var hdr=document.querySelector('.site-header');
    var nav=document.querySelector('.main-nav');
    if(hdr&&nav){nav.style.top=hdr.getBoundingClientRect().bottom+'px';}
    var open=body.classList.toggle('nav-open');
    toggle.setAttribute('aria-expanded',open?'true':'false');
  });}
  document.querySelectorAll('.has-dd > .dd-toggle').forEach(function(btn){
    btn.addEventListener('click',function(e){
      var li=btn.parentElement;var open=li.classList.toggle('open');
      btn.setAttribute('aria-expanded',open?'true':'false');
    });
  });
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape'){body.classList.remove('nav-open');document.querySelectorAll('.has-dd.open').forEach(function(li){li.classList.remove('open')});}
  });
  document.querySelectorAll('form.js-form').forEach(function(form){
    function show(kind){
      form.querySelectorAll('.form-status').forEach(function(n){n.classList.toggle('show',n.getAttribute('data-status')===kind);});
      var n=form.querySelector('.form-status[data-status="'+kind+'"]');
      if(n){n.scrollIntoView({behavior:'smooth',block:'center'});}
    }
    form.addEventListener('submit',function(e){
      if(!form.checkValidity()){return;}
      var endpoint=form.getAttribute('data-endpoint');
      if(!endpoint){e.preventDefault();show('unconnected');return;}
      if(!window.fetch||!window.FormData){return;}
      e.preventDefault();
      var btn=form.querySelector('button[type="submit"]');
      var label=btn?btn.innerHTML:'';
      if(btn){btn.disabled=true;btn.textContent='Sending\u2026';}
      var ajax=endpoint.replace('formsubmit.co/','formsubmit.co/ajax/');
      fetch(ajax,{method:'POST',body:new FormData(form),headers:{'Accept':'application/json'}})
        .then(function(r){return r.json().then(function(j){return {ok:r.ok,j:j};});})
        .then(function(res){
          if(res.ok&&res.j&&String(res.j.success)==='true'){form.reset();show('success');}
          else{show('error');}
        })
        .catch(function(){show('error');})
        .then(function(){if(btn){btn.disabled=false;btn.innerHTML=label;}});
    });
  });
  var y=document.getElementById('year');if(y){y.textContent=new Date().getFullYear();}
})();
