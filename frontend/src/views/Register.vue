<template>
  <div class="background">
      <div class="grandParentContaniner">
          <div class="registertrationFormContainer">
           <form
            @submit="register"
            >
            <h1>Register your account</h1><br>
              <label for="username">Username</label><br>
              <input type="text" id="username" name="username"><br>
              <label for="email">Email address</label><br>
              <input type="email" id="email" name="email"><br>
              <label for="password">Password</label><br>
              <input type="password" id="password" name="password"><br>
              <label for="confirmpwd">Confirm password</label><br>
              <input type="password" id="confirmpwd" name="confirmpwd"><br>
               <button type="submit" @click="register">Submit</button> 
            </form>
            <div class="line"></div>
            <div class="login-text">
            <p>Already have an account? <a href="/login">Log in.</a></p>
            </div>
      </div>
    </div>
  </div>
</template>

<script>
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
      register: async function(e){
        e.preventDefault()
        if (!password.value || !this.validate(password.value, confirmpwd.value)) return false
        const response = await fetch('http://localhost:8000/api/v1/users/', {
          method: 'POST', // *GET, POST, PUT, DELETE, etc.
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: username.value,
            password: password.value,
            email: email.value,
            favorites: []
          }) // body data type must match "Content-Type" header
        });
        return response.json();
      }
    }
  }
</script>

<style scoped>

	.grandParentContaniner{
		display:flex;
    margin: 0 auto; ;
    justify-content: center;
    align-items: center;
	}
    
  .background {
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%), linear-gradient(to top, #000000 0%, #ffffff 100%);
  }
  .registertrationFormContainer {
      display: flex;
      flex-direction: column;
      background-color: #ffffff;
      padding: 40px;
      margin-top: 100px;
      margin-bottom: 40px;
  }
  .line {
    margin-top: 26px;
    border-top: 1px solid;
  }
  .login-text {
    display: flex;
    justify-content: center;
  }
  input {
      box-sizing: border-box;
  }

  button {
    box-shadow: none;
    border: none;
    max-width: 380px;
    padding-left: 30px;
    padding-right: 30px;
    height: 60px;
    border-radius: 30px;
    background-color: #3098f3;
    opacity: 0.7;
    color: #ffffff;
    font-family: "Poppins";
    font-style: italic;
    font-size: 30px;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 2.16px;
    display: block;
    margin: auto;
    margin-top: 26px;
    cursor: pointer;
    float: right;
  }
  button:disabled {
    opacity: 0.1;
  }
  button:hover {
    opacity: 1;
  }

</style>