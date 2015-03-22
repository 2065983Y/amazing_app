var clicked = {};
var grid = clickableGrid(document.getElementById("id_rows").value, document.getElementById("id_cols").value, function(el,row,col,i){
    //console.log("You clicked on element:",el);
    //console.log("You clicked on row:",row);
    //console.log("You clicked on col:",col);
    //console.log("You clicked on item #:",i);
    //el.className='clicked';
    //var rows = parseInt(document.getElementById("rows").innerHTML);
    //var cols = parseInt(document.getElementById("cols").innerHTML);
    console.log(document.getElementById("id_rows").value);
    console.log(document.getElementById("id_cols").value);
    if(el.className=="clicked")
    {
        el.className=" "
    }
    else
    {
        el.className='clicked'
    }
    //if (lastClicked) lastClicked.className='';
    //lastClicked = el;
    var square=row.toString().concat(col.toString());
    if(square in clicked)
        delete clicked[square];
    else
        clicked[square] = {"row": row, "col": col}

    document.getElementById("cells").setAttribute("value", displayCells(rows, cols, clicked));
});

function displayCells(rows, cols, clicked)
{
    var cells = "";
    console.log("rows", rows);
    console.log("cols", cols);
    for(var r=0;r<rows;r++)
    {
        for(var c=0;c<cols;c++)
        {
            var key = r.toString().concat(c.toString());
            if(key in clicked)
            {
                //console.log(clicked[key]);
                if(clicked[key]["row"] == r && clicked[key]["col"] == c)
                {
                    cells = cells.concat("1");
                    continue;
                }
            }
            cells = cells.concat("0");
        }
    }
    console.log(cells);
    return cells;
}

document.body.appendChild(grid);

function clickableGrid( rows, cols, callback ){
    var i=0;
    var grid = document.createElement('table');
    grid.className = 'grid';
    for (var r=0;r<rows;++r){
        var tr = grid.appendChild(document.createElement('tr'));
        for (var c=0;c<cols;++c){
            var cell = tr.appendChild(document.createElement('td'));
            cell.addEventListener('click',(function(el,r,c,i){
                return function(){
                    callback(el,r,c,i);
                }
            })(cell,r,c,i),false);
        }
    }
    return grid;
}