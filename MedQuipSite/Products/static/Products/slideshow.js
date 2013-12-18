$('.ppt li:gt(0)').hide();
			$('.ppt li:last').addClass('last');
			$('.ppt li:first').addClass('first');

			var cur = $('.ppt li:first');
			var ppt = $('.ppt');
			var interval;
			
			$('#fwd').click( function() {
				goFwd();
			} );

			$('#back').click( function() {
				goBack();
			} );
			$('#1').click( function() {
				if (cur.attr('id') != 'mainImage1'){
					cur.fadeOut( 1000 );
					cur = $("#mainImage1");
					//cur = document.getElementById("mainImage1");
					cur.fadeIn( 1000 );
					setColors();
				}
			} );
			$('#2').click( function() {
				if (cur.attr('id') != 'mainImage2'){
					cur.fadeOut( 1000 );
					cur = $("#mainImage2");
					//cur = document.getElementById("mainImage2");
					cur.fadeIn( 1000 );
					setColors();
				}
			} );
			function setColors(){
			var children = $('#pptButtons').children();
				for (var i=1;i<children.length-1;i++){ 
					
					$(children[i]).css('background-color','#d3d3d3');
					if(cur.attr('id').replace('mainImage','') == i){
						$(children[i]).css('background-color','#c43f3f');
					}
				}
				//$(cur).css('background-color','#c43f3f');
			}

			function back() {
				cur.fadeOut( 1000 );
				if ( cur.attr('class') == 'first' )
					cur = $('.ppt li:last');
				else
					cur = cur.prev();
				cur.fadeIn( 1000 );
			}

			function forward() {
				cur.fadeOut( 1000 );
				if ( cur.attr('class') == 'last' )
					cur = $('.ppt li:first');
				else
					cur = cur.next();
				cur.fadeIn( 1000 );
				setColors();
			}

			function start() {
				interval = setInterval( "forward()", 10000 );
				setColors();
			}
			function stop() {
				clearInterval( interval );
			}
			
			function goFwd() {
				stop();
				forward();
				start();
			}
			function goBack() {
				stop();
				back();
				start();
			}
			
			$(function() {
				start();
			} );