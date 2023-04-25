/* 
    Promise 객체 사용법
    new Promise((resolve, reject) => {
        
        if (성공) {
        return resolve(value) => 비동기 작업이 성공했을 때 리턴하고 싶은 값을 value로
        } else if (실패조건) {
        return reject(value) => 비동기 작업이 실패했을 때 리턴하고 싶은 값을 value로
        }
    })

    axios.get() 이 함수도 return 값이 Promise 객체였기 때문에 .then, .catch 사용 가능

*/

const water = function() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("A: 물을 넣는다.")
            return resolve(["물"])
            // return reject("물을 너무 많이 넣었다.")
        }, Math.random() * 2000 + 1000);
    })
}

const soup = function(ramen) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("현재 재료: ", ramen)
            console.log("B: 스프을 넣는다.")
            ramen.push("스프")
            return resolve(ramen)
        }, Math.random() * 2000 + 1000);
    })
}


const noodle = function(ramen) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("현재 재료: ", ramen)
            console.log("C: 면을 넣는다.")
            ramen.push("면")
            return resolve(ramen)
        }, Math.random() * 2000 + 1000);
    })
}

// 물 => 스프 => 면
water()
.then((ramen) => {
    return soup(ramen)
})

.then((ramen) => {
    return noodle(ramen)
})

.then((ramen) => {
    // 위의 모든 작업이 끝나고 나서 하고 싶은 일
    console.log("라면 끓이기 시작 : ", ramen)
})

.catch((err) => {
    console.log("라면 만드는 도중에 문제 발생: ", err)
})

// 최신문법 async, await
/* 사용방법
    await는 해당 비동기 작업이 끝나면 사용할 수 있도록 해주는 키워드
    비동기 함수 async 아래서만 사용 가능
*/
// const makeRamen = async function() {
//     const ramen = await water()
//     .then((ramen) => {
//         return soup(ramen)
//     })
    
//     .then((ramen) => {
//         return noodle(ramen)
//     })
    
//     .then((ramen) => {
//         // 위의 모든 작업이 끝나고 나서 하고 싶은 일
//         console.log("라면 끓이기 시작 : ", ramen)
//     })
    
//     .catch((err) => {
//         console.log("라면 만드는 도중에 문제 발생: ", err)
//     })
//     // return ramen
//     // const result = makeRamen();
//     console.log("라면 : ", ramen)
// }

// makeRamen()
