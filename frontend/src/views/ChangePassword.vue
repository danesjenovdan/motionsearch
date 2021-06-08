<template>
  <div class="login-container background">
    <div class="wrapper">
      <div class="debate-logo">
        <router-link to="/"><img src="../assets/motion-generator-logo.svg" alt="motion generator logo"></router-link>
        <span>Easiest way to find a motion for debating</span>
      </div>
      <div class="registration-form-container">
        <form @submit="change">
          <h1>Enter new password</h1>
          <label for="password">Password</label>
          <input type="password" id="password" name="password">
          <button type="submit">Change password</button>
        </form>
        <hr class="line"/>
        <div class="login-text">
          <p><router-link to="/login">Back to log in.</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        password: '',
        favorites: []
      }
    },
    props: ['uid', 'token'],
    methods : {
      change: async function(e){
        e.preventDefault()
        const response = await this.$store.dispatch('change', {
            password: password.value,
            token: this.$route.params.token, 
            uid: this.$route.params.uid
          })
        if (response) this.$router.push('/login')
      }
    }
  }
</script>
<style scoped>
</style>
