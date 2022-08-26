from orator.migrations import Migration


class CreateCompaniesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('companies') as table:
            table.increments('id')
            table.integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.string('name')
            table.string('catchPhrase')
            table.string('bs')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('companies')
