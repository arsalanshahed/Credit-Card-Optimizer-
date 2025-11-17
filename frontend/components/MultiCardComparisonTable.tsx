'use client';

import { motion } from 'framer-motion';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Info } from 'lucide-react';
import type { CardRecommendation } from '@/lib/types';
import { formatCurrency, formatPercentage } from '@/lib/formatting';
import { Award, TrendingUp } from 'lucide-react';

interface MultiCardComparisonTableProps {
  recommendations: CardRecommendation[];
  bestCard?: CardRecommendation;
  onViewDetails?: (card: CardRecommendation) => void;
}

export default function MultiCardComparisonTable({
  recommendations,
  bestCard,
  onViewDetails,
}: MultiCardComparisonTableProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.2 }}
    >
      <Card className="glass border-purple-500/20 shadow-xl">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <TrendingUp className="w-5 h-5 text-purple-400" />
            Card Comparison
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="overflow-x-auto">
            <Table>
              <TableHeader>
                <TableRow className="border-purple-500/20">
                  <TableHead className="text-purple-300">Card</TableHead>
                  <TableHead className="text-purple-300">Issuer</TableHead>
                  <TableHead className="text-purple-300">Reward Rate</TableHead>
                  <TableHead className="text-purple-300">Annual Fee</TableHead>
                  <TableHead className="text-purple-300">Monthly Rewards</TableHead>
                  <TableHead className="text-purple-300">Annual Rewards</TableHead>
                  {onViewDetails && (
                    <TableHead className="text-purple-300">Actions</TableHead>
                  )}
                </TableRow>
              </TableHeader>
              <TableBody>
                {recommendations.map((card, index) => {
                  const isBest = bestCard?.card_name === card.card_name;
                  return (
                    <motion.tr
                      key={card.card_name}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ delay: index * 0.05 }}
                      className={`border-purple-500/10 ${isBest ? 'bg-purple-500/10' : ''}`}
                    >
                      <TableCell className="font-semibold">
                        <div className="flex items-center gap-2">
                          {isBest && <Award className="w-4 h-4 text-yellow-400" />}
                          {card.card_name}
                          {isBest && (
                            <Badge className="bg-gradient-to-r from-purple-600 to-pink-600">
                              Best
                            </Badge>
                          )}
                        </div>
                      </TableCell>
                      <TableCell>{card.issuer}</TableCell>
                      <TableCell>
                        <span className="font-bold text-purple-400">
                          {formatPercentage(card.reward_rate)}
                        </span>
                      </TableCell>
                      <TableCell>
                        {card.annual_fee > 0 ? (
                          <span className="text-red-400">{formatCurrency(card.annual_fee)}</span>
                        ) : (
                          <span className="text-green-400">$0</span>
                        )}
                      </TableCell>
                      <TableCell className="font-semibold text-green-400">
                        {formatCurrency(card.estimated_monthly_rewards)}
                      </TableCell>
                      <TableCell className="font-semibold text-green-400">
                        {formatCurrency(card.estimated_annual_rewards)}
                      </TableCell>
                      {onViewDetails && (
                        <TableCell>
                          <Button
                            variant="outline"
                            size="sm"
                            onClick={() => onViewDetails(card)}
                            className="border-purple-500/50 hover:bg-purple-500/10"
                          >
                            <Info className="w-3 h-3 mr-1" />
                            Details
                          </Button>
                        </TableCell>
                      )}
                    </motion.tr>
                  );
                })}
              </TableBody>
            </Table>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  );
}

