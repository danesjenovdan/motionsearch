<template>
    <div class="container">
      <div :class="['filterBox', { selected: true }]">
        <img src="../assets/topic.svg">
        <i><span class="filterTitle" :onclick="togglePopup"> Topic </i></span>
         <div class="popup">
            <div class="popup-container" id="myPopup">
              <div class="popup-box">
                <div class="checkmark-container">
                  <div v-for="category in categories" :key="category">
                    <input :id="category" type='checkbox'/>
                    {{category}}
                  </div>
                </div>
              <div class="popup-apply"> Apply</div>
              </div>
              <div class="popup-arrow">
              </div>
            </div>
        </div> 
      </div>
      <div class="filterBox">
        <img src="../assets/difficulty.svg">
        <span class="filterTitle"><i> Difficulty </i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/format.svg">
        <span class="filterTitle"><i> Format </i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/age.svg">
        <span class="filterTitle"><i> Age </i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/type.svg">
        <span class="filterTitle"><i> Motion type </i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/focus.svg">
        <span class="filterTitle"><i> Training  focus</i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/impro.svg">
        <span class="filterTitle"><i> Either impro or prep </i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/keyword.svg">
        <span class="filterTitle"><i> Keyword </i></span>
      </div>
      <div class="filterBox">
        <img src="../assets/random.svg">
        <span class="filterTitle"><i> Show me a random motion </i></span>
      </div>
    </div>
</template>

<script>

  export default {
    data() {
      return {
        categories: [
          'Art and Culture',
          'Criminal Justice System',
          'Business',
          'Development',
        ]
      }
    },
    methods: {
      togglePopup: (event) => {
        var popup = document.getElementById("myPopup");
        popup.classList.toggle("show");
      }
    }
  }
</script>

<style scoped>
  .container {
    margin: 80px 0px 40px 0px;
    display: grid;
    grid-template-columns: 30% 30% 30%;
    column-gap: 3%;
    row-gap: 3%;
  }
  .checkmark-container {
    margin: 80px 0px 40px 0px;
    display: grid;
    grid-template-columns: 50% 50%;
    column-gap: 3%;
    row-gap: 3%;
  }
  .popup-apply{
    border-top: 1px solid black;
  }
  .selected {
    border: 4px solid #3098f3;
  }
  .filterBox {
    display: flex;
    flex-direction: column;
    background-color: white;
    align-items: center;
    padding: 50px;
  }
  .filterTitle {
    color: #252525;
    font-family: "IBM Plex Mono";
    font-size: 24px;
    font-weight: 400;
    font-style: normal;
    letter-spacing: normal;
    line-height: 26px;
    text-align: center;
  }
  .filterTitle:hover {
    cursor: pointer;
  }

   /* Popup container */
  .popup {
    position: relative;
    display: inline-block;
    cursor: pointer;
  }

  .popup-box {
    height: 80%;
    margin: 10px;
  }

  .popup-arrow {
    content: "";
    width: 20px;
    height: 20px;
    transform: rotate(-45deg);
    background: #fff;
    position: absolute;
    z-index: 1;
    border-left: 4px solid #3098f3;
    border-bottom: 4px solid #3098f3;
    margin-left: 20px;
    margin-top: -1px;
  }


/* The actual popup (appears on top) */
  .popup .popup-container {
    visibility: hidden;
    background-color: white;
    color: black;
    border: 4px solid #3098f3;
    text-align: center;
    padding: 8px 0;
    position: absolute;
    z-index: 2;
    bottom: 300%;
    left: 50%;
    margin-left: -80px;
  }

/* Popup arrow */
  .popup .popuptext::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    z-index: -1;
    border-color: #555 transparent transparent transparent;
  }

  /* Toggle this class when clicking on the popup container (hide and show the popup) */
  .popup .show {
    visibility: visible;
    -webkit-animation: fadeIn 1s;
    animation: fadeIn 1s
  }

  /* Add animation (fade in the popup) */
  @-webkit-keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
  }

  @keyframes fadeIn {
    from {opacity: 0;}
    to {opacity:1 ;}
  } 

</style>