( function( $ ) {

	// ...
	// ANALYZER
	// ...
	var $result = $( 'div#analyzing-result' );
	var $loading = $result.find( 'div#loading' );

	$( document ).on( 'submit', 'form#analyzing-form', function( event ) {
		event.preventDefault();

		var target = $( event.target ).attr( 'action' );
		var url = $( event.target ).find( 'input[name=url]' ).val();
		var csrf = $( event.target ).find( 'input[name=csrfmiddlewaretoken]' ).val();
		var $button = $( event.target ).find( 'button[type=submit]' );
		
		if ( url ) {
			$.ajax({
				method: 'POST',
				url: target,
				data: {
					csrfmiddlewaretoken: csrf,
					url: url,
				},
				beforeSend: function( xhr ) {
					$button.attr( 'disabled', true );
					$loading.removeClass( 'd-none' );
					$result.find( 'div#result' ).html( '' );
				},
				success: function( response ) {
					var keywords = [];
					var warnings = [];

					$.each( response.keywords, function( k, v) {
						keywords.push(`<span class="badge bg-success flex align-items-center">${v[1]} | <span>${v[0]}</span></span>`);
					});

					$.each( response.warnings, function( k, v) {
						warnings.push(`<li>${v}</li>`);
					});

					var $output = `
						<table class="table">
							<tr>
								<td>Word count</td>
								<td>${response.word_count}</td>
							</tr>

							<tr>
								<td>Page title</td>
								<td>${response.title}</td>
							</tr>

							<tr>
								<td>Meta description</td>
								<td>${response.description}</td>
							</tr>

							<tr>
								<td>Keyword on-page</td>
								<td>${keywords.join(' ')}</td>
							</tr>

							<tr>
								<td>Number of Internal Links</td>
								<td>${response.internal_link_count}</td>
							</tr>

							<tr>
								<td>Warnings</td>
								<td>
									<ol>
										${warnings.join('')}
									</ol>
								</td>
							</tr>
						</table>
					`;

					$result.find( 'div#result' ).html( $output );
				},
				failure: function( error ) {
					
				},
				complete: function() {
					$button.removeAttr( 'disabled' );
					$loading.addClass( 'd-none' );
				}
			});
		}
	});

} )( jQuery );