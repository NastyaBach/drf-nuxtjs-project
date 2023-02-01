
<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
    <nuxt-link class="navbar-brand" to="/">
      <img src="/img/icon.jpg" width="40" height="40" alt="logo">
    </nuxt-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <h5>
            <nuxt-link class="nav-link" to="/contact">Контакты</nuxt-link>
          </h5>
        </li>
        <li class="nav-item ">
          <h5>
            <nuxt-link class="nav-link" to="/">Главная</nuxt-link>
          </h5>
        </li>
      </ul>
      <form class="form-inline my-2 my-lg-0">
        <input name="q" v-model="q" type="text" class="form-control mr-sm-2" placeholder="Поиск" aria-label="Поиск">
        <button class="btn btn-outline-success my-2 my-sm-0 mr-2" type="submit" @click.stop.prevent="submit()">Поиск</button>
      </form>
      <span class="navbar-text mr-2" v-if="user">{{user.username}}</span>
      <span v-if="loggedIn"><nuxt-link class="btn btn-outline-dark mr-2" to="/signout">Выход</nuxt-link></span>
      <span v-else>
        <nuxt-link class="btn btn-outline-dark mr-2" to="/signin">Вход</nuxt-link>
        <nuxt-link class="btn btn-outline-dark mr-2" to="/signup">Регистрация</nuxt-link>
      </span>
    </div>
  </nav>
</template>

<script>
export default {
  data(){
    return {
      q : null,
    }
  },
  methods: {
    submit(){
      this.$router.push("/search?q="+this.q);
    }
  },
  computed: {
    loggedIn() {
      return this.$auth.loggedIn
    },
    user() {
      return this.$auth.user
    }
  }
}
</script>

<style scoped>

</style>