'use client';

import { motion } from 'framer-motion';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { useAppStore } from '@/lib/store';
import { formatCurrency } from '@/lib/formatting';
import { Trash2, Calendar } from 'lucide-react';
import { Button } from '@/components/ui/button';

export default function DashboardPage() {
  const { savedSimulations, deleteSimulation } = useAppStore();

  return (
    <div className="min-h-screen py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-12"
        >
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Dashboard
          </h1>
          <p className="text-xl text-gray-300">
            Your saved simulations and analytics
          </p>
        </motion.div>

        {savedSimulations.length === 0 ? (
          <Card className="glass border-purple-500/20 text-center py-12">
            <p className="text-gray-400 mb-4">No saved simulations yet</p>
            <p className="text-sm text-gray-500">
              Create a simulation in the Optimizer to save it here
            </p>
          </Card>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {savedSimulations.map((simulation) => (
              <motion.div
                key={simulation.id}
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                className="glass border-purple-500/20 rounded-xl p-6 hover:border-purple-500/40 transition-all"
              >
                <div className="flex items-start justify-between mb-4">
                  <div className="flex items-center gap-2 text-sm text-gray-400">
                    <Calendar className="w-4 h-4" />
                    {new Date(simulation.timestamp).toLocaleDateString()}
                  </div>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => deleteSimulation(simulation.id)}
                    className="text-red-400 hover:text-red-300"
                  >
                    <Trash2 className="w-4 h-4" />
                  </Button>
                </div>

                <h3 className="text-lg font-semibold text-white mb-4">
                  {simulation.recommendations[0]?.card_name || 'No card selected'}
                </h3>

                <div className="space-y-2 mb-4">
                  <div className="flex justify-between text-sm">
                    <span className="text-gray-400">Total Monthly Spend</span>
                    <span className="text-white font-semibold">
                      {formatCurrency(
                        Object.values(simulation.spend).reduce((a, b) => a + b, 0)
                      )}
                    </span>
                  </div>
                  {simulation.recommendations[0] && (
                    <div className="flex justify-between text-sm">
                      <span className="text-gray-400">Best Card Rewards</span>
                      <span className="text-green-400 font-semibold">
                        {formatCurrency(
                          simulation.recommendations[0].estimated_monthly_rewards
                        )}
                        /mo
                      </span>
                    </div>
                  )}
                </div>

                <div className="pt-4 border-t border-purple-500/20">
                  <p className="text-xs text-gray-500 mb-2">Spending Breakdown</p>
                  <div className="space-y-1">
                    {Object.entries(simulation.spend)
                      .filter(([_, value]) => value > 0)
                      .map(([category, value]) => (
                        <div
                          key={category}
                          className="flex justify-between text-xs"
                        >
                          <span className="text-gray-400 capitalize">
                            {category.replace('_', ' ')}
                          </span>
                          <span className="text-gray-300">
                            {formatCurrency(value)}
                          </span>
                        </div>
                      ))}
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
