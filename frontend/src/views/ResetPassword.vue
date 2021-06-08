<template>
  <div class="login-container background">
    <div class="wrapper">
      <div class="debate-logo">
        <router-link to="/"><img src="../assets/motion-generator-logo.svg" alt="motion generator logo"></router-link>
        <span>Easiest way to find a motion for debating</span>
      </div>
      <div class="registration-form-container">
        <form @submit="reset">
          <h1>Enter the email address associated with your account, and we’ll email you a link to reset your password.</h1>
          <label for="email">Email address</label>
          <input type="email" id="email" name="email">
          <button type="submit">SEND RESET LINK</button>
        </form>
        <hr class="line"/>
        <div class="login-text">
          <p> <router-link to="/login">Back to log in.</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        email: '',
        favorites: []
      }
    },
    methods : {
      reset: async function(e){
        e.preventDefault()
        const response = await this.$store.dispatch('reset', {
            email: email.value,
          })
        if (response) this.$router.push('/login')

      }
    }
  }
</script>
<style scoped>
</style>
