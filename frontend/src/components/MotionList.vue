<template>
    <div class="parent-container">
        <div class="header"> 
          <button type="submit">SUGGEST A MOTION</button> 
          <button class="login" type="submit">LOG IN</button> 
        </div>
        <div class="line"/>
        <div class="parentContainer">
          <div class="left">
            <h3>Motions</h3>
              <div class="motions-container" v-for="motion in motions" :key="motion._id">
                <p class="motions-date">Added on {{motion.date}}</p>
                <p class="motions-title">{{motion.text}}</p>
                <div>
              </div>
            </div>
          </div>
    </div>
  </div>
</template>

<script>
  const tags = [
        'culture', 
        'sport',
        'employment',
        'europian union',
        'culture', 
        'sport',
        'employment',
        'europian union'
      ]
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
    components: [
    ],
    data() {
      return {
        tags,
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
            console.log('motions: ', motions);
      },
      removeUsedWhere: (index) => {
        usedWhere.splice(index, 1)
      }
    }
  }

</script>

<style scoped lang="scss">

    .header {
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: end;
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
    border-bottom: 1px solid black;

  }

  .motions-container {
    border-bottom: 1px solid black;
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
  .textAreaContainer{
    display:inline-block;
    position:relative;
    margin-bottom: 20px;
  }

  .textAreaButton {
    position:absolute;
    bottom:0px;
    right:10px;
    background:none;
    border:none;
    margin:0;
    padding:0;
    cursor: pointer;
    color: #3098f3;
    font-family: Poppins;
    font-size: 18px;
    font-weight: 700;
    font-style: normal;
    letter-spacing: normal;
    line-height: normal;
    text-align: left;
    text-decoration: underline;
  }

  textarea {
    display: block;
    resize: none;
    width: 100%;
    height: 100%; 
    box-sizing: border-box;
  }

	.parent-container {
		display:flex;
    margin: 0 auto;
    flex-direction: column;
    justify-content: center;
    align-items: initial;
	}
  .favourite{
    background-image: '../assets/favourite.svg';
  }
  .background {
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%), linear-gradient(to top, #000000 0%, #ffffff 100%);
  }
  .shareContainer {
    display: flex;
    flex-direction: row;
    background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
  }
  .parentContainer {
      display: flex;
      flex-direction: row;
      overflow: hidden;
  }
  .motionButtons {
    display:flex;
    justify-content: space-between;
  }
  .links {
    background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
    padding: 20px;
    margin-left: 20px;
    margin-top: 20px;
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
  .tags {
    list-style: none;
    margin-top: 20px;
    overflow: hidden; 
    padding: 0;
  }
  .tag {
    display: inline-block;
    padding-left: 10px;
    padding-right: 10px;
    margin: 10px;
    border-radius: 14px;
    border: 2px solid #3098f3;
  }
  .tag-text {
    color: #000000;
    font-family: "IBM Plex Mono";
    font-size: 14px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 18px;
    text-align: center;
  }
  input {
    box-sizing: border-box;
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