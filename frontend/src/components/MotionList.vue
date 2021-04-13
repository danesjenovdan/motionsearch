<template>
    <div class="parent-container">
        <div class="header"> 
          <button class="login" type="submit">LOG IN</button> 
          <button type="submit">SUGGEST A MOTION</button> 
        </div>
        <div class="line"/>
        <div class="motions-container">
          <div class="left">
            <div class="motions-title-bar">
              <h3>Motions</h3>
              <div class="motions-sort">
                <p>Sort by</p>
                <div class="sort-button"><span class="sort-button-text"><b>Date Added</b></span></div>
                <div class="sort-button"><span class="sort-button-text"><b>Quality</b></span></div>
              </div>
            </div>
            <div class="motions-list" v-for="motion in motions" :key="motion._id">
              <div class="motion-text-container">
                <p class="motions-date">Added on {{motion.date}}</p>
                <p class="motions-title">{{motion.text}}</p>
              </div>
              <div class="votes">
                <voting/>
              </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
  import Voting from './Voting.vue'
  const motions = [
      {
        _id: "first", 
        username: "Pekoči janez",
        date: "21/7/2021",
        text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      },
      {
        _id: "second", 
        username: "Pekoči janez",
        date: "21/7/2021",
        text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      },
      {
        _id: "third", 
        username: "Pekoči janez",
        date: "21/7/2021",
        text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      },
      {
        _id: "third", 
        username: "Pekoči janez",
        date: "21/7/2021",
        text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      }
      ]
  export default {
    components: {
      Voting
    },
    data() {
      return {
        motions,

      }
    },
    methods: {
      addUsedWhere: () => {
        motions.push(
          {
            _id: "second", 
        username: "Pekoči janez",
        date: "21/7/2021",
        text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      }
        )
      },
      removeUsedWhere: (index) => {
        usedWhere.splice(index, 1)
      }
    }
  }

</script>

<style scoped lang="scss">

  .header {
    margin-right: 40px;
  }
  .motions-title-bar {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    border-bottom: 1px solid black;
  }
  .motions-sort {
    display: flex;
    flex-direction: row;
    align-items: center;
  }
    .share-bar {
    position: relative;
    width: 100%;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    padding: 20px;
    // background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
    background-image: linear-gradient(-62deg, #cee7fd 0%, #f7fafd 100%);
    z-index: 2;
    .share-bar-split {
        width: 100%;
        display: flex;
        flex-direction: row;
        display: flex;
        flex-wrap: wrap;
        align-content: center;
        &.hidden {
        display: none !important;
        }
    }
    h1 {
        margin-top: 0;
        // width: 100%;
    }
    input {
        margin-left: 20px;
    }
    }
  h3 {
    color: #252525;
    font-family: "Poppins";
    font-size: 30px;
    font-weight: 700;
    font-style: normal;
    letter-spacing: normal;
    line-height: 60px;
    text-align: left;
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
  }
  .sort-button {
    /* Style for "Rounded Re" */
    border-radius: 20px;
    background-color: rgb(48, 152, 243, 0.2);
    padding: 10px;
    margin-left: 10px;
    cursor: pointer;
  }
  .sort-button-text {
    color: #000000;
    font-family: "IBM Plex Mono";
    opacity: 1;
    font-size: 14px;
    font-weight: 400;
    font-style: italic;
    letter-spacing: normal;
    line-height: 18px;
    text-align: center;
    text-transform: uppercase;
  }
  .motions-list {
    border-bottom: 1px solid black;
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .motions-date {
    color: #252525;
    font-family: "IBM Plex Mono";
    font-size: 14px;
    font-style: italic;
    letter-spacing: normal;
    line-height: 18px;
    text-align: left;
  }
  .motions-title {
    color: #252525;
    font-family: Poppins;
    font-size: 24px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    text-align: left;
  }
  .votes {
    width: 78px;
    height: 78px;
    flex-shrink: 0;
    margin-right: 20px;
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%);
  }
	.parent-container {
		display:flex;
    margin: 0 auto;
    flex-direction: column;
    justify-content: center;
    align-items: initial;
    overflow-x: auto;
	}
  .favourite{
    background-image: '../assets/favourite.svg';
  }
  .background {
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%), linear-gradient(to top, #000000 0%, #ffffff 100%);
  }

  .motions-container {
      display: flex;
      flex-direction: row;
      overflow: hidden;
      padding: 0px 40px 0px 40px;
  }
  .motionButtons {
    display:flex;
    justify-content: space-between;
  }

  .left {
    display: flex;
    flex-direction: column;
    overflow-y: auto;
  }

  .line {
    margin-top: 26px;
    margin-bottom: 30px;
    border-top: 1px solid #3098f3;
    margin-left: 0px;
    margin-right: 0px;
  }
  input {
    box-sizing: border-box;
  }
  .motion-text-container {
    display: flex;
    flex-direction: column;
  }
  .motion-text {
    /* Style for "EU member" */
    color: #252525;
    font-family: Poppins;
    font-size: 48px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 60px;
    text-align: left;;
  }
    .login {
      border: 4px solid #ffcc00;
      background-color: #ffffff;
      color: #000000;
    }
  a {
    /* Style for "Lorem Ipsu" */
    color: #252525;
    font-family: Poppins;
    font-size: 18px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 40px;
    text-align: left;
    text-decoration: underline;
    /* Text style for "Lorem Ipsu" */
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
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
    margin-left: 25px;
    margin-top: 26px;
    cursor: pointer;
    float: right;
    white-space: nowrap;
  }
  button:disabled {
    opacity: 0.1;
  }
  button:hover {
    opacity: 1;
  }

</style>