$(function () {
    let update_url = '/car/update/';
    $('#add').click(function () {
        let $car_id = $(this).attr('car_id');
        let $input = $(this).prev('input');
        let $td1 = $('#sum_price');
        let value = parseInt($input.val()) < parseInt($input.attr('max'))
            ? parseInt($input.val()) + 1
            : parseInt($input.attr('max'));
        if (parseInt($input.val()) < parseInt($input.attr('max'))) {
            $.post(update_url, {'ac': 1, 'car_id': $car_id}, function (result) {
                if (result.status === 200) {
                    $input.val(value);
                    $td1.text(result.sum_price)
                }
            })
        }
    });
    $('#sub').click(function () {
        let $car_id = $(this).attr('car_id');
        let $input = $(this).next('input');
        let $td1 = $('#sum_price');
        let value = $input.val() > 1
            ? $input.val() - 1
            : 1;
        $.post(update_url, {ac: 2, 'car_id': $car_id}, function (result) {
            if (result.status === 200) {
                $input.val(value);
                $td1.text(result.sum_price)
            }
        })
    });
});