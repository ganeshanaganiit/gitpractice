const second= document.querySelector("#sec");
const millisec= document.querySelector("#milli");
const start= document.querySelector(".start");
const stop = document.querySelector(".stop");
const reset= document.querySelector("#reset");
var sec=0;
var milli=0;
var timeInterval;

const timer=()=>{
    milli++
    if(milli<9){
        millisec.innerHTML="0"+milli;

    }
    if(milli>9){
        millisec.innerHTML=milli;
    }
    if(milli>99){
        sec++;
        second.innerHTML= "0" +sec;
        milli=0;
        millisec.innerHTML="0"+0;
    }
    if(sec>9){
        second.innerHTML=sec;
    }
    
}

start.addEventListener("click", ()=>{
    timeInterval=setInterval(timer, 10);

})

stop.addEventListener("click", ()=>{
    clearInterval(timeInterval);
})


// reset.classList.add("reset");
reset.addEventListener("click", ()=>{
    clearInterval(timeInterval);
    sec=00;
    milli=00;
    second.innerHTML= "0" +sec;
    millisec.innerHTML= "0"+milli;

})

