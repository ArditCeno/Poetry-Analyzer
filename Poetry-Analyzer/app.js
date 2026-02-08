const poem=document.getElementById("poem");
const topk=document.getElementById("topk");
const btn=document.getElementById("analyzeBtn");
const res=document.getElementById("results");
const status=document.getElementById("status");

btn.onclick=async()=>{

if(!poem.value)return alert("Paste poem");

status.innerText="Analyzing...";

const r=await fetch("http://localhost:8080/analyze",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({text:poem.value,top_k:+topk.value})
});

const data=await r.json();
res.innerHTML="<pre>"+JSON.stringify(data,null,2)+"</pre>";
status.innerText="Done";
};
