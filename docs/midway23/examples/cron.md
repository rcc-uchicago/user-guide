# Cron-like jobs

Cron jobs persist until they are canceled or encounter an error.
The Midway2 cluster has a dedicated partition, `cron`, for running
Cron jobs. Please email [help@rcc.uchicago.edu](mailto:help@rcc.uchicago.edu) to request submitting
Cron-like jobs. These jobs are subject to scheduling limits and will
be monitored.

Here is an example of an sbatch script that runs a Cron job (see also
`cron.sbatch`):

```bash
#!/bin/bash

#SBATCH --time=00:05:00
#SBATCH --output=cron.log
#SBATCH --open-mode=append
#SBATCH --account=cron-account
#SBATCH --partition=cron
#SBATCH --qos=cron

# Specify a valid Cron string for the schedule. This specifies that
# the Cron job run once per day at 5:15a.
SCHEDULE='15 5 * * *'

# Here is an example of a simple command that prints the host name and
# the date and time.
echo "Hello on $(hostname) at $(date)."

# This schedules the next run.
sbatch --quiet --begin=$(next-cron-time "$SCHEDULE") cron.sbatch
```

After executing a simple command (print the host name, date and time),
the script schedules the next run with another call to `sbatch` with
the `--begin` option.
