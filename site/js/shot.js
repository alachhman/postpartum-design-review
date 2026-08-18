/* Verification harness: ?shot=<n> isolates the nth .stage on the page at 1:1
   so screenshots can be inspected at real device resolution. No effect on
   normal viewing. */
(function(){
  var m = /[?&]shot=(\d+)/.exec(location.search);
  if(!m) return;
  var i = parseInt(m[1],10);
  var stages = document.querySelectorAll('.stage');
  var s = stages[i];
  if(!s){ document.body.innerHTML='<pre style="color:#fff;font:14px monospace">no stage '+i+' (have '+stages.length+')</pre>'; return; }
  var st = document.createElement('style');
  st.textContent = 'body>*{display:none!important}body::after{display:none!important}'+
    'html,body{margin:0;padding:0;background:#0E0D0C!important;overflow:hidden}'+
    '#shotholder{display:block!important;position:fixed;inset:0;display:flex!important;'+
    'align-items:center;justify-content:center}'+
    '#shotholder .stage{--s:1!important}';
  document.head.appendChild(st);
  var h = document.createElement('div'); h.id='shotholder';
  h.appendChild(s); document.body.appendChild(h);
})();

/* ?audit=1 — reports any phone screen whose content overflows the 852pt canvas,
   plus any tap target under 44pt. Read via chrome --dump-dom. */
(function(){
  if(!/[?&]audit=1/.test(location.search)) return;
  window.addEventListener('load',function(){ setTimeout(function(){
    var out=[];
    document.querySelectorAll('.screen').forEach(function(sc,i){
      var body=sc.querySelector('.body');
      if(body && body.scrollHeight > body.clientHeight+1){
        out.push('OVERFLOW screen#'+i+' by '+(body.scrollHeight-body.clientHeight)+'px');
      }
      sc.querySelectorAll('button,a').forEach(function(b){
        var h=b.offsetHeight; /* layout px — unaffected by the display transform */
        if(h>0 && h<44) out.push('SMALLTAP screen#'+i+' '+h+'pt "'+(b.textContent||'').trim().slice(0,28)+'"');
      });
    });
    var d=document.createElement('div'); d.id='AUDIT';
    d.textContent = out.length? out.join(' | ') : 'CLEAN';
    document.body.appendChild(d);
  },400);});
})();
