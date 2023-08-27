var youtubePlayer;

// Function to load YouTube API
function loadYouTubeAPI() {
  var tag = document.createElement('script');
  tag.src = 'https://www.youtube.com/iframe_api';
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
}

// Function to extract video ID from URL or embed link
function getYouTubeVideoId(url) {
  var videoId = '';
  if (url.indexOf('youtube.com') !== -1) {
    var match = url.match(/v=([^&]+)/);
    if (match) {
      videoId = match[1];
    }
  } else if (url.indexOf('youtu.be') !== -1) {
    var match = url.match(/youtu.be\/([^&]+)/);
    if (match) {
      videoId = match[1];
    }
  }
  return videoId;
}

// Function to create YouTube player
function createYouTubePlayer(videoUrl) {
  var videoId = getYouTubeVideoId(videoUrl);
  if (videoId !== '') {
    youtubePlayer = new YT.Player('player', {
      height: '100%',
      width: '100%',
      videoId: videoId,
      events: {
        'onStateChange': onPlayerStateChange
      }
    });

    document.getElementById('video-container').style.display = 'block';
  } else {
    alert('Invalid YouTube video URL or embed link.');
  }
}

// Function to handle YouTube player state change
function onPlayerStateChange(event) {
  if (event.data === YT.PlayerState.ENDED) {
    closeVideoPlayer();
  }
}

// Function to close video player
function closeVideoPlayer() {
  document.getElementById('video-container').style.display = 'none';
  var player = document.getElementById('player');
  player.innerHTML = '';

  // Stop the video playback
  if (youtubePlayer) {
    youtubePlayer.stopVideo();
    youtubePlayer = null;
  }
}

// Function to handle "Watch Trailer" button click
function handleWatchTrailerClick(event) {
  event.preventDefault();
  var trailerUrl = this.getAttribute('data-trailer-url');
  if (typeof YT !== 'undefined' && YT.loaded) {
    createYouTubePlayer(trailerUrl);
  } else {
    alert('YouTube API is not available. Please try again later.');
  }
}

// Load YouTube API
loadYouTubeAPI();

// Add event listeners to the "Watch Trailer" buttons
var watchTrailerButtons = document.querySelectorAll('.watch-trailer');
watchTrailerButtons.forEach(function (button) {
  button.addEventListener('click', handleWatchTrailerClick);
});
