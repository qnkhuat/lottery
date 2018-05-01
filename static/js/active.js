function addmore() {
    var el = '<input type="number" name="number" placeholder="Số"  class="form-control number " required><input type="number" name="amount" placeholder="Điểm"  class="form-control amount" required>'
    $("#insert").append(el);     // Append new elements
    console.log('added');
}
