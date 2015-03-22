var clicked = {};

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
                    cells = cells.concat("0");
                    continue;
                }
            }
            cells = cells.concat("1");
        }
    }
    console.log(cells);
    return cells;
}

function generateMaze()
{
    if(document.getElementById("id_rows").value)
    {
        if(document.getElementById("id_cols").value)
        {

            var grid = clickableGrid(parseInt(document.getElementById("id_rows").value),
                                    parseInt(document.getElementById("id_cols").value), function(el,row,col,i){
                //console.log("You clicked on element:",el);
                //console.log("You clicked on row:",row);
                //console.log("You clicked on col:",col);
                //console.log("You clicked on item #:",i);
                //el.className='clicked';
                var rows = parseInt(document.getElementById("id_rows").value);
                var cols = parseInt(document.getElementById("id_cols").value);
                //console.log(document.getElementById("id_rows").value);
                //console.log(document.getElementById("id_cols").value);
                if(el.className=="wall")
                {
                    el.className=" "
                }
                else
                {
                    el.className='wall'
                }
                //if (lastClicked) lastClicked.className='';
                //lastClicked = el;
                var square=row.toString().concat(col.toString());
                if(square in clicked)
                    delete clicked[square];
                else
                    clicked[square] = {"row": row, "col": col}

                document.getElementById("id_cells").value = displayCells(rows, cols, clicked).toString();
            });

            document.body.appendChild(grid);
            document.getElementById("clickme").style.visibility="hidden";
            return;
        }
    }
    alert("enter");
}

document.getElementById("clickMe").onclick = generateMaze;

function clickableGrid( rows, cols, callback ){
    var i=0;
    var grid = document.createElement('table');
    console.log(rows);
    console.log(cols);
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