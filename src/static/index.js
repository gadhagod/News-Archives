function search_day(){
    var day = document.getElementById('day').value;
    document.write('loading..');
    if (day === ''){
        window.location.replace('/');
    } else {
        window.location.replace('/day/' + day);
    }
}
function search_keyword(){
    var keyword = document.getElementById('keyword').value;
    document.write('loading..');
    if (keyword === ''){
        window.location.replace('/');
    } else {
        window.location.replace('/keyword/' + keyword);
    }
}