// $('.btn-search').click(function(){
//     console.log(1)
//     $.post('/blog/search',
//         {
//             search_param:$('.search-bar').val(),
//         })
// })

// $('.btn-search').click(function(){
//     console.log(1)
//     $.ajax({
//         type:'post',
//         url:'/blog/search',
//         async: false,
//         data:{
//             search_param:$('.search-bar').val(),
//         }
//     })
// })

(function () {
    $.get("/blog/tags", function (data, status) {
        for (let i = 0; i < data.length; i++) {
            let tag_id = data[i].id
            let tag_str = '/blog/tag/'+tag_id
            $('.tags_list').append('<a class="item" href="#">' + data[i].name + '</a>')
            $('.tags_list .item').last().attr("href",tag_str)
        }

    });
})();

(function () {
    $.get("/blog/classifies", function (data, status) {
        for (let i = 0; i < data.length; i++) {
            let classify_id = data[i].id
            let classify_str = '/blog/classify/'+classify_id
            $('.classifies_list').append('<a class="item" href="#">' + data[i].name + '</a>')
            $('.classifies_list .item').last().attr("href",classify_str)
        }

    });
})();