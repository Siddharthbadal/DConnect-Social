let LoginBtn= document.getElementById('login-btn')
let LogoutBtn= document.getElementById('logout-btn')

let token = localStorage.getItem('token')
if (token){
    LogoutBtn.remove()
}else{
    LoginBtn.remove()
}



logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location= 'file:///E:/django/Django-2021-master/project/dcircle/frontend/login.html'
})



let projectsUrl = "http://127.0.0.1:8000/api/projects/"
let getProjects = ()=>{
    fetch(projectsUrl)
    .then(response => response.json())
    .then(data => {
        
        buildProjects(data)
    })
}


let buildProjects = (projects)=>{
    let projectsWrapper = document.getElementById('projects-wrapper')
    for (let i=0; projects.length > i; i++){
        let project = projects[i]
        
        let projectCard =`
            <div class="project--card">
            <img src="http://127.0.0.1:8000${project.image}" />
                <div>
                    <div class="project--header">
                        <h1>${project.title}</h1>
                        <strong class="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
                        <strong class="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
                        
                    </div>
                    <i>${project.vote_ratio} Votes<i/>
                    <p>${project.description.substring(100)}</p>
                </div>

            </div>
        `
        projectsWrapper.innerHTML += projectCard
    }
    addVoteEvents()
}


let addVoteEvents = () => {
    
    let voteBtns = document.getElementsByClassName('vote--option')
    for (let i=0; voteBtns.length > i; i++){
        voteBtns[i].addEventListener('click', (e)=> {
            let token = localStorage.getItem('token')
            console.log(token)
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project

            console.log(vote)
            console.log(project)

            fetch(`http://127.0.0.1:8000/api/projects/${project.id}/vote/`,{
                method:"POST",
                headers:{
                    'Content-Tyep': 'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({'value': vote})
                
            })
            .then(response => response.json())
            .then(data =>{
                getProjects()
                console.log('Success', data)
            })
        })
    }
}


getProjects()