(() => {
    const ENDPOINT = '/tweets/';

    const app = new Vue({
        el: '#app',
        data: {
            tweets: [],
            username: '',
            msg: '',
        },
        methods: {
            insertTweet: function () {
                fetch(ENDPOINT, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({name: this.username, message: this.msg})
                }).then(rs => rs.json()).then(rs => {
                    this.tweets.unshift(rs);
                    this.msg = '';
                }).catch(er => {
                    console.error(er)
                })
            }
        },
        mounted() {
            fetch(ENDPOINT)
                .then(rs => rs.json())
                .then(rs => {
                    console.log(rs);
                    app.tweets = rs
                })
                .catch(er => console.log(er))

        }

    });
})();