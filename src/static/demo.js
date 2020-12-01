function search_day(){
    var day = document.getElementById('day').value;
    document.write('loading..');
    if (day === ''){
        window.location.href = 'demo/';
    } else {
        window.location.href = 'demo/day/' + day;
    }
}
function search_keyword(){
    var keyword = document.getElementById('keyword').value;
    document.write('loading..');
    if (keyword === ''){
        window.location.href = 'demo/';
    } else {
        window.location.href ='demo/keyword/' + keyword;
    }
}