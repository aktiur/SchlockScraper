var scrollSpeed = 200;

function scrollToNew () {
  var scrollTop = $(window).scrollTop();
  $('h4').each(function(i, h4){ // loop through article headings
    var h4top = $(h4).offset().top; // get article heading top
    if (scrollTop+10 < h4top) { // compare if document is below heading
      $.scrollTo(h4, scrollSpeed); // scroll to in .8 of a second
      return false; // exit function
    }
  });
}

function scrollToLast () {
  var scrollTop = $(window).scrollTop();

  var scrollToThis = null;

  // Find the last element with class 'new' that isn't on-screen:
  $('h4').each(function(i, h4) {
    var h4top = $(h4).offset().top;
    if (scrollTop > h4top) {
      // This one's not on-screen - make a note and keep going:
      scrollToThis = h4;
    } else {
      // This one's on-screen - the last one is the one we want:
      return false;
    }
  });

  // If we found an element in the loop above, scroll to it:
  if(scrollToThis != null) {
    $.scrollTo(scrollToThis, scrollSpeed);
  }
}

function scrollDown() {
	// determine active div
	var scrollTop = $(window).scrollTop();
	var windowHeight = $(window).height();
	
	var activeDiv = null;
	var divH = 0;
	var divT = 0;
	
	var scrolling = 0;
	
	$('div.comic, h3').each(function(i, div) {
		divH = $(div).height();
		divT = $(div).offset().top;
		if((scrollTop+windowHeight/2 >= divT) && (scrollTop+windowHeight/2 <= divT + divH)) {
			activeDiv = div;
			return false;
		}
	});
	
	if(divT + divH > scrollTop + windowHeight) {
		// if bottom of comic not visible
		scrolling = Math.min(divT+divH-.9*windowHeight, scrollTop+.75*windowHeight)
		$.scrollTo(scrolling, scrollSpeed, {axis:'y'});
	} else {
		// if bottom of comic is visible, jump to next
		activeDiv = $(activeDiv).nextAll('div.comic');
		if(activeDiv.length > 0) {
			divT = $(activeDiv).offset().top;
			divH = $(activeDiv).height();
			if(divH > windowHeight) {
				scrolling = divT - .1*windowHeight;
			} else {
				scrolling = divT + (divH-windowHeight)/2;
			}
			$.scrollTo(scrolling, scrollSpeed, {axis:'y'});
		}
	}
}

function scrollUp() {
	// determine active div
	var scrollTop = $(window).scrollTop();
	var windowHeight = $(window).height();
	
	var activeDiv = null;
	var divH = 0;
	var divT = 0;
	
	var scrolling = 0;
	
	$('div.comic, h3').each(function(i, div) {
		divH = $(div).height();
		divT = $(div).offset().top;
		if((scrollTop+windowHeight/2 >= divT) && (scrollTop+windowHeight/2 <= divT + divH)) {
			activeDiv = div;
			return false;
		}
	});
	
	if(divT < scrollTop) { // if top of comic not visible
		scrolling = Math.max(divT-.1*windowHeight, scrollTop-.75*windowHeight)
		$.scrollTo(scrolling, scrollSpeed, {axis:'y'});
	} else { // if top of comic is visible, jump to previous
		activeDiv = $(activeDiv).prevAll('div.comic');
		if(activeDiv.length > 0) {
			divT = $(activeDiv).offset().top;
			divH = $(activeDiv).height();
			if(divH > windowHeight) {
				scrolling = divT+divH - .9*windowHeight;
			} else {
				scrolling = divT + (divH-windowHeight)/2;
			}
			$.scrollTo(scrolling, scrollSpeed, {axis:'y'});
		}
	}	
}

jQuery(function () {

  $(document).keydown(function (evt) {
    if (evt.keyCode == 74) { // J key
      evt.preventDefault(); // prevents the usual scrolling behaviour
      scrollToNew(); // scroll to the next new heading instead
    } else if (evt.keyCode == 75) { // K key
      evt.preventDefault();
      scrollToLast();
	} else if (evt.keyCode == 68) { // D key
	  evt.preventDefault();
	  scrollDown();
	} else if (evt.keyCode == 70) { // F key
	  evt.preventDefault();
	  scrollUp();
    } else if (evt.keyCode == 66) { // B key
	  evt.preventDefault();
	  if(localStorage.getItem('bookmark')) {
	    window.location.href = localStorage.getItem('bookmark');
      }
	}
  });
});

function bookmarkLink(link) {
	return '<a href="' + link + '">Go to bookmark</a> | <button onclick="removeBookmark();">Remove bookmark</button>';
}

function setBookmark(link) {
	localStorage.setItem('bookmark', link);
	$('#bookmark').html(bookmarkLink(link));
}

function removeBookmark() {
	localStorage.removeItem('bookmark');
	$('#bookmark').html("You don't have set a bookmark yet!");
}

jQuery(function () {
	if(localStorage.getItem('bookmark')) {
		setBookmark(localStorage.getItem('bookmark'));
	}
});

jQuery(function () {
	$('a.setbookmark').click(function(e) {
		e.preventDefault();
		var file = document.location.pathname.match(/[^\/]+$/)[0];
		setBookmark(file + '#' + $(this).data('anchor'));
	});
});