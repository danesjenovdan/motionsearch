<template>
    <div class="motionCommentsContainer">
      <div class="header">
        <div class="logo">
          <img src="../assets/motion-generator-logo.svg" alt="motion generator logo">
        </div>
        <div class="header-buttons">
          <router-link to="/motionSuggest" class="btn">Suggest a motion</router-link>
          <router-link to="/login" class="btn login">Log in</router-link>
        </div>
      </div>
        <div class="share-bar">
          <div class="share-bar-split">
            <h1>Share this motion!</h1>
            <input type="url" class="share-input" :value="`https://djnd.si/sideflip/#`">
          </div>
        </div>
        <div class="parentContainer">
          <div class="left">
            <h3>Comments</h3>
              <div class="textAreaContainer">
                <textarea rows="3" cols="20" name="comment" form="usrform"> Write your comment here!
                </textarea>
                  <button class="textAreaButton" v-on:click="addUsedWhere()">Submit</button>
              </div>
              <p v-for="el in usedWhere" :key="el">{{el}}</p>
              <div class="commentContainer" v-for="comment in comments" :key="comment._id">
                <i><p>{{comment.username}} | {{comment.date}}</p></i>
                <p>{{comment.text}}</p>
                <div>
              </div>
            </div>
          </div>
            <div class="right">
              <div class="links">
                <h3>Where was it used</h3>
                  <a href="http://google.com">googe</a><br/>
                  <a href="http://google.com">google</a><br/>
                  <a href="http://google.com">googe</a><br/>
                </div>
              <div class="links">
                <h3>Links</h3>
                  <a href="http://google.com">googe</a><br/>
                  <a href="http://google.com">google</a><br/>
                  <a href="http://google.com">googe</a><br/>
                </div>
            </div>
    </div>
  </div>
</template>

<script>
  const comments = [
      {
        _id: "first",
        username: "Pekoči janez",
        date: "21/7/2021",
        text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      },
      /*{
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
      }*/
      ]
  export default {
    components: [
    ],
    data() {
      return {
        comments,

      }
    },
    methods: {
      addUsedWhere: () => {
        comments.push(
          {
            _id: "second",
        username: "Pekoči janez",
        date: "21/7/2021",
        text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      }
        )
            console.log('comments: ', comments);
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
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  background-color: #FFFFFF;
  border-bottom: 1px solid #3098f3;
  // margin-bottom: 30px;

  @media (min-width: 768px) {
    justify-content: flex-end;
    padding: 20px;
    position: static;
  }

  @media (min-width: 1200px) {
    padding: 30px;
  }

  .logo {
    @media (min-width: 768px) {
      display: none;
    }

    img {
      height: 50px;
    }
  }
}

  .share-bar {
    position: relative;
    overflow: hidden;
    margin: 30px 20px 0 20px;
    display: flex;
    flex-direction: row;
    padding: 20px;
    // background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
    background-image: linear-gradient(-62deg, #cee7fd 0%, #f7fafd 100%);
    z-index: 2;

    @media (min-width: 1200px) {
      margin: 30px 40px 0 40px;
    }

    .share-bar-split {
      width: 100%;
      align-content: center;
      &.hidden {
        display: none !important;
      }

      @media (min-width: 1200px) {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
      }
    }
    h1 {
      margin-top: 0;
      margin-right: 20px;
    }
  }
  .share-input {
    min-width:0; /* Remove the automatic minimum size set so the element can shrink*/
    width: 100%; /* Set any value of width here as reference*/
    flex: 1; /* make the item grow to fill the remaining space */
  }

  .commentContainer {
    border: 1px solid black;
    padding: 20px;
  }
  .textAreaContainer{
    display:inline-block;
    position:relative;
    margin-bottom: 20px;
  }

  .textAreaButton {
    position:absolute;
    bottom:0;
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
    text-decoration: underline;
    height: 60px;
  }

  textarea {
    display: block;
    resize: none;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
  }

	.motionCommentsContainer {
		display:flex;
    margin: 0 auto;
    flex-direction: column;
    justify-content: center;
    align-items: initial;
	}
  .shareContainer {
    display: flex;
    flex-direction: row;
    background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
  }
  .parentContainer {
    display: flex;
    flex-direction: column-reverse;
    margin: 10px 20px 40px 20px;
    overflow: hidden;

    @media (min-width: 1200px) {
      margin: 10px 40px 40px 40px;
    }

    @media (min-width: 1200px) {
      flex-direction: row;
    }
  }
  .motionButtons {
    display:flex;
    justify-content: space-between;
  }
  .links {
    background-image: linear-gradient(-62deg, #f2f6fa 0%, #dbe7f1 100%);
    padding: 20px;
    margin-top: 20px;

    h3 {
      margin-top: 0;
      color: #252525;
      font-family: "Poppins";
    }

    @media (min-width: 1200px) {
      margin-left: 20px;
    }
  }
  .left {
    display: flex;
    flex-direction: column;
    overflow-y: auto;

    @media (min-width: 1200px) {
      flex: 2 1 0;
    }

    h3 {
      color: #252525;
      font-family: "Poppins";
      margin-top: 40px;

      @media (min-width: 1200px) {
        font-size: 30px;
      }
    }
  }
  .right {
    width: 100%;

    @media (min-width: 1200px) {
      flex: 1 1 0;
    }
  }

.line {
  margin: 0 0 30px;
  border-top: 1px solid #3098f3;
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


</style>
