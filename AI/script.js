var c = 0;

function tick()
{
    c++;
    document.getElementById('stepsdone').value = c;
  //  movewall(); //move wall to the left
}

var tickinterval;

function runsim(state)
{
    if(state == 1)//run simulation
    {
        if(c > 100)
        {
            runsim('0'); //force stop
        }else{
                tickinterval = setinterval(tick(), 100);
             }
        
    }else{
            //stop simulation
            clearInterval(tickinterval);
            c = 0;
            document.getElementById('stepsDone').value = c;
           
         }
}
/*
function moveWall()
{
    var getWallX = document.getElementById('wall').offsetLeft;
    
    document.getElementById('debugTextarea').innerHTML += "["+c+"] Wall PosX: "+getWallX+"\n";
    document.getElementById('debugTextarea').scrollTop = document.getElementById('debugTextarea').scrollHeight;
    
    if(getWallX <= 0)
    {
        document.getElementById('wall').style.left = null;
        document.getElementById('wall').style.right = '0px';
    }else{
            getWallX = getWallX-40;
            document.getElementById('wall').style.left = getWallX+'px';
         }
    
}






