
const pageLinks = document.querySelectorAll('.pageNum')
const next = document.getElementById('nextPage');
const previous = document.getElementById('prevPage');

//fill in keyword param if it exists
let url_string = window.location.href;
let url = new URL(url_string)
document.getElementById("keyword").value = url.searchParams.get("keyword")

//set current page link to active css class
let currentpage = parseInt(url.searchParams.get("page"))
for (let i=0;i<pageLinks.length; i++){
    if (parseInt(pageLinks[i].dataset.pagenum) == currentpage){
        pageLinks[i].className = pageLinks[i].className + " active";
    }
}

//event listeners for the slider controls/thumbnails
for (let i=0;i<pageLinks.length; i++){
    pageLinks[i].addEventListener('click', (evt)=>{ 
        pagenum = evt.target.dataset.pagenum;
        url.searchParams.set("page", pagenum)
        window.location.href = url //redirect to new url
        
    });
}

if (next) {
    next.addEventListener('click', (evt)=>{
        //get the current page number and call the function to go to next page
        //prevent going above max page number
        let currentpage = parseInt(url.searchParams.get("page"))
        if (currentpage != pageLinks.length){
            url.searchParams.set("page", currentpage+1);
            window.location.href = url;
        }
        
    });
}

if (previous) {
    previous.addEventListener('click', (evt)=>{
        //get the current page number and call the function to go to the previous page
        //prevent going below page 1
        let currentpage = parseInt(url.searchParams.get("page"))
        if (currentpage > 1){
            url.searchParams.set("page", currentpage-1);
            window.location.href = url;
        }
        
    });
}

