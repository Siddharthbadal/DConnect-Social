let tags = document.getElementsByClassName('project-tag')

    for(let i = 0; tags.length>i; i++){
         tags[i].addEventListener('click', (e)=>{
            let tagId = e.target.dataset.tag
            let projectId = e.target.dataset.project

            fetch('https://dconnect.onrender.com//api/remove-tag/',{
            method: 'DELETE',
            headers:{
                'content-type': 'application/json'
            },
            body:JSON.stringify({'project': projectId, 'tag':tagId})
        }).then(response => response.json())
        .then(data => {
            e.target.remove()
        })
         })

    }
