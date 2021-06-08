<template>
  <div class="login-container background">
    <div class="wrapper">
      <div class="debate-logo">
      <router-link to="/"><img src="../assets/motion-generator-logo.svg" alt="motion generator logo"></router-link>
        <span>Easiest way to find a motion for debating</span>
      </div>
      <div class="registration-form-container">
        <form @submit="register">
          <h1>Register your account</h1>
          <label for="username">Username</label>
          <input type="text" id="username" name="username">
          <label for="email">Email address</label>
          <input type="email" id="email" name="email">
          <label for="password">Password</label>
          <input type="password" id="password" name="password">
          <label for="confirmpwd">Confirm password</label>
          <input type="password" id="confirmpwd" name="confirmpwd">
          <button type="submit" @click="register">Submit</button>
        </form>
        <hr class="line"/>
        <div class="login-text">
          <p>Already have an account?  <router-link to="/login">Log in.</router-link></p>
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
        confirmpwd: '',
        email: '',
        favorites: []
      }
    },
    methods : {
      validate(password, confirmpwd) {
        return password === confirmpwd
      },
      validateEmail(email) {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        const isValid =  re.test(String(email).toLowerCase());
        if(!isValid) toast.error("Email is not in the correct format.");
        return isValid
      },
      validateForm(username, email) {
        if(!username) toast.error("Username is required.");
        if(!email) toast.error("Email is required.");

        return username !== null && email !== null
      },
      register: async function(e){
        e.preventDefault()
        if (!password.value || !this.validate(password.value, confirmpwd.value)) { 
          toast.error("Passwords do not match, please try again.");
          return false;
          }
        if(!this.validateForm(username.value, email.value)) return false;
        if (!this.validateEmail(email.value)) return false;
        const response = await this.$store.dispatch('register', {
            username: username.value,
            password: password.value,
            email: email.value,
          })
        if (response) this.$router.push('/login')
      }
    }
  }
</script>

<style scoped lang="scss">
</style>
