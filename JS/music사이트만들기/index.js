/* 
  아래에 코드를 작성해주세요.
  
Application name	java
API key	fbb82622a2e03d85afd6fc5ee614804f
Shared secret	328b07dc539f8fd9c5443fdc968dcea0
Registered to	lkg2097

*/

const searchBtn = document.querySelector(".search-box__button")

const fetchAlbums = (page=1, limit=10) => {
  const keyword = document.querySelector(".search-box__input").value
  // alert("브라우저에서 확인!")

  API_key = "fbb82622a2e03d85afd6fc5ee614804f"
  const API_address = `http://ws.audioscrobbler.com/2.0/?method=album.search&album=believe&api_key=${API_key}&page=${page}&limit=${limit}&format=json`
  axios.get(API_address)
  .then((response) => {
    const albums = response.data.results.albummatches
    console.log(albums)
  })
  .catch((response) => {
    alert("잠시후 다시 시도해주세요")
  })


}

searchBtn.addEventListener("click", fetchAlbums)


