function scrollToNew () {
  scrollTop = $(window).scrollTop();
  $('h4').each(function(i, h4){ // loop through article headings
    h4top = $(h4).offset().top; // get article heading top
    if (scrollTop+10 < h4top) { // compare if document is below heading
      $.scrollTo(h4, 300); // scroll to in .8 of a second
      return false; // exit function
    }
  });
}

function scrollToLast () {
  scrollTop = $(window).scrollTop();

  var scrollToThis = null;

  // Find the last element with class 'new' that isn't on-screen:
  $('h4').each(function(i, h4) {
    h4top = $(h4).offset().top;
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
    $.scrollTo(scrollToThis, 300);
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