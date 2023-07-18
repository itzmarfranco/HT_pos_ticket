odoo.define('ht_pos_ticket.pos_ticket_modification', function (require) {
    var PosTicket = require('point_of_sale.models').PosTicket;

    PosTicket.include({
        // Override or add methods here to modify the POS ticket
        // Example:
        get_header: function () {
            var header = this._super();
            header += '<div class="your-custom-class">Custom Header Content</div>';
            return header;
        },
    });

});
