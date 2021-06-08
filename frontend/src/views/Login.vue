<template>
  <div class="login-container background">
    <div class="wrapper">
      <div class="debate-logo">
      <router-link to="/"><img src="../assets/motion-generator-logo.svg" alt="motion generator logo"></router-link>
         <span>Easiest way to find a motion for debating</span>
      </div>
      <div class="registration-form-container">
        <form @submit="login">
          <h1>Please log in to contribute to use Motion Generator features.</h1>
          <label for="username">Username</label>
          <input type="text" id="username" name="username">
          <label for="password">Password</label>
          <input type="password" id="password" name="password">
          <div class="password-reset-text">
            <router-link to="/reset" class="link">Forgot your password?</router-link>
          </div>
          <button class="login" type="submit">LOG IN</button>
        </form>
        <hr class="line"/>
        <div class="login-text">
          <p>Don't have an account? <router-link to="/register" class="link">Register now.</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
  import { useToast } from "vue-toastification";

  const toast = useToast();
  export default {
    data() {
      return {
        username: '',
        password: '',
      }
    },
    methods : {
      login: async function(e){
        e.preventDefault()
        try {
          const response = await this.$store.dispatch('login', {username: username.value, password: password.value})
          if (response) this.$router.push('/')
        } catch (error) {
          console.log('error: ', error);
        }
      }
    }
  }
</script>

<style scoped lang="scss">
</style>
