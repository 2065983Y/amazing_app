var path = {};

function hasNeighbour(row, col, path)
{
    var toTest = (row-1).toString().concat(col.toString());
    if( toTest in path )
    {
        if(path[toTest]["row"] == row - 1 && path[toTest]["col"] == col)
            return true;
    }
    toTest = (row + 1).toString().concat(col.toString());
    if( toTest in path)
    {
        if(path[toTest]["row"] == row + 1 && path[toTest]["col"] == col)
            return true;
    }
    toTest = row.toString().concat((col - 1).toString());
    if( toTest in path )
    {
        if(path[toTest]["row"] == row && path[toTest]["col"] == col - 1)
            return true;
    }
    toTest = row.toString().concat((col + 1).toString());
    if( toTest in path)
    {
        if(path[toTest]["row"] == row && path[toTest]["col"] == col + 1)
            return true;
    }
    return false;
}

var grid = drawMaze(document.getElementById("rows").getAttribute("value"), document.getElementById("cols").getAttribute("value"),
                                                                            function(el,row,col,i){
    var rows = document.getElementById("rows").getAttribute("value");
    var cols = document.getElementById("cols").getAttribute("value");
    if(el.className == "wall")
    {
        console.log("Wall clicked");
        return;
    }
    var square=row.toString().concat(col.toString());
    if(! hasNeighbour(row, col, path))
    {
        console.log("cannot get there");
        return;
    }
    if(el.className == "path")
    {
        alert(" Still not supporting deletion of steps, please be patient");
    }
    else
    {
        el.className="path"
    }
    if(row == rows - 1 && col == cols - 1)
    {
        alert("nailed it!");
    }
//    if(square in path)
//       delete path[square];
//    else
        path[square] = {"row": row, "col": col}

    //document.getElementById("cells").setAttribute("value", displayCells(rows, cols, clicked));
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
                if(clicked[key]["row"] == r && clicked[key]["col"] == c)
                {
                    cells = cells.concat("1");
                    continue;
                }
            }
            cells = cells.concat("0");
        }
    }
    return cells;
}

document.body.appendChild(grid);

function drawMaze( rows, cols, callback ){
    var cells = document.getElementById("cells").getAttribute("value");
    var i=0;
    var grid = document.createElement('table');
    grid.className = 'grid';
    for (var r=0;r<rows;++r){
        var tr = grid.appendChild(document.createElement('tr'));
        for (var c=0;c<cols;++c){
            var cell = tr.appendChild(document.createElement('td'));
            if(cells[r*rows + c]==0)
            {
                cell.className="wall"
            }
            cell.addEventListener('click',(function(el,r,c,i){
                return function(){
                    callback(el,r,c,i);
                }
            })(cell,r,c,i),false);
        }
    }

    var start = grid.firstChild.firstChild;
    start.className = "path";
    path["00"] = { "row":0, "col":0 };

    return grid;
}