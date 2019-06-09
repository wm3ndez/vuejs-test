(() => {
    const app = new Vue({
        el: '#app',
        data: {
            tweets: [{
                id: 1,
                name: 'John Doe',
                created_at: new Date(),
                message: `Hello, World! I'm using Vue`
            }]
        }
    })
})();