<template>
 <div class="split-container">
      <div class="split left">
          <motion/>
      </div>
      <div class="split hidden-xs">
        <motion-comments/>
      </div>
    </div>
</template>

<script>
  import Motion from '../components/Motion.vue'
  import MotionComments from '../components/MotionComments.vue'

  export default {
  components: {
    Motion,
    MotionComments
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
  .hidden-xs {
    height:90vh;
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