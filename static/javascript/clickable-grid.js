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
                if(clicked[key]["row"] == r && clicked[key]["col"] == c)
                {
                    cells = cells.concat("0");
                    continue;
                }
            }
            cells = cells.concat("1");
        }
    }
    console.log("cells", cells);
    return cells;
}


function generateMaze()
{
    var grid = clickableGrid(parseInt(document.getElementById("id_rows").value),
                            parseInt(document.getElementById("id_cols").value), function(el,row,col,i){

        var rows = parseInt(document.getElementById("id_rows").value);
        var cols = parseInt(document.getElementById("id_cols").value);

        el.className = el.className=="wall"? " ": "wall";

        var square=row.toString().concat(col.toString());
        if(square in clicked)
            delete clicked[square];
        else
            clicked[square] = {"row": row, "col": col}

        document.getElementById("id_cells").value = displayCells(rows, cols, clicked).toString();
    });

    document.body.appendChild(grid);
}


function clickableGrid( rows, cols, callback ){
    var i=0;
    var previous = document.getElementsByTagName('table')[0];
    if(previous)
    {
        previous.parentNode.removeChild(previous);
    }

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


document.getElementById("clickMe").onclick = generateMaze;
