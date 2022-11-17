// Colours

const addColorPickerEventListeners = () => {

$('#color').on('change', function(e) {

    $('#color-value').text(e.target.value);

});

$('#bg-color').on('change', function(e) {

    $('#bg-color-value').text(e.target.value);

});


};

//Sliders

addColorPickerEventListeners();

const addSliderEventListeners = () => {

$('#size').on('change', function(e) {

$('#size-value').text(`${e.target.value} x ${e.target.value}`);

});

$('#margin').on('change', function(e) {

    $('#margin-value').text(`${e.target.value} px`);
    
    });

};

addSliderEventListeners();

//API parameters

const prepareParameters = params => {
    const prepared = {
        data: params.data,
        size: `${params.size}x${params.size}`,
        color: params.color.replace('#', ''),
        bgcolor: params.bgColor.replace('#', ''),
        qzone: params.qZone,
        format: params.format,
    };

    return prepared;
};


const displayQrCode = imgUrl => {

$('#qr-code-settings').addClass('flipped');
$('#qr-code-result').addClass('flipped');
$('#qr-code-image').attr('src', imgUrl);

};

const getQrCode = parameters => {
    const baseUrl = 'https://api.qrserver.com/v1/create-qr-code/';
    const urlParams = new URLSearchParams(parameters).toString();

    const fullUrl = `${baseUrl}?${urlParams}`;

    fetch(fullUrl).then(response => {
        if (response.status === 200) {
            displayQrCode(fullUrl);
        }
    });
};

const showInputError = () => {

$('#data').addClass('error');

};

const dataInputEventListener = () => {

$('#data').on('change', function(e) {

if (e.target.value !== '') {

    $('#data').removeClass('error');
    $('#cta').removeAttr('disabled');


} else {

    $('#data').addClass('error');
    $('#cta').attr('disabled', true);

}

});

};

dataInputEventListener();

const onSubmit = () => {
    const data = $('#data').val();

    if (!data.length) {
        return showInputError();
    }

    const color = $('#color').val();
    const bgColor = $('#bg-color').val();
    const size = $('#size').val();
    const qZone = $('#margin').val();
    const format = $('input[name=format]:checked').val();

    const parameters = prepareParameters({ data, color, bgColor, size, qZone, format });

    getQrCode(parameters);
};

const addSubmitEventListener = () => {
    $('#cta').on('click', onSubmit);
};

addSubmitEventListener();

const onEdit = () => {
$('#qr-code-settings').removeClass('flipped');
$('#qr-code-result').removeClass('flipped');
};

const addEditEventListener = () => {

    $('#edit').on('click', onEdit);

};

addEditEventListener();
