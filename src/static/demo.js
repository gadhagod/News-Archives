function search_day(){
    var day = document.getElementById('day').value;
    document.write('loading..');
    if (day === ''){
        window.location.replace('demo/');
    } else {
        window.location.replace('demo/day/' + day);
    }
}
function search_keyword(){
    var keyword = document.getElementById('keyword').value;
    document.write('loading..');
    if (keyword === ''){
        window.location.replace('demo/');
    } else {
        window.location.replace('demo/keyword/' + keyword);
    }
}