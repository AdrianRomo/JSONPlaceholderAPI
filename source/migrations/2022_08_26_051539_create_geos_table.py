from orator.migrations import Migration


class CreateGeosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('geos') as table:
            table.increments('id')
            table.integer('address_id').unsigned()
            table.foreign('address_id').references('id').on('addresses')
            table.float('lat')
            table.float('lng')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('geos')
